from django.test import TestCase
from django.urls import reverse

from .models import Message
from bots.models import Bot


class BotTestCase(TestCase):
    def setUp(self):
        bot = Bot.objects.create(
            id='36b9f842-ee97-11e8-9443-0242ac120002',
            name='bot'
        )
        user = Bot.objects.create(
            id='16edd3b3-3f75-40df-af07-2a3813a79ce9',
            name='user'
        )
        Message.objects.create(
            conversationId = '7665ada8-3448-4acd-a1b7-d688e68fe9a1',
            from_bot = bot.id,
            to = user.id,
            text = '"Oi! Como posso te ajudar?',
        )
    
    def test_messages_id_unique(self):
        message = Message.objects.all()[0]
        unique = message._meta.get_field('id').unique
        self.assertTrue(unique)

    def test_messages_id_max_length(self):
        message = Message.objects.all()[0]
        max_length = message._meta.get_field('id').max_length
        self.assertEquals(max_length, 36)

    def test_messages_get(self):
        response = self.client.get('/messages/')
        self.assertEqual(response.status_code, 200)

    def test_messages_get_by_id(self):
        message = Message.objects.all()[0]
        response = self.client.get(f'/messages/{message.id}/')
        self.assertEqual(response.status_code, 200)

    def test_messages_get_by_conversationId(self):
        message = Message.objects.all()[0]
        response = self.client.get(f'/messages/?={message.conversationId}')
        self.assertEqual(response.status_code, 200)

    def test_messages_post(self):
        bot = Bot.objects.get(name='bot')
        user = Bot.objects.get(name='user')
        response = self.client.post('/messages/', {
            'conversationId': '7665ada8-3448-4acd-a1b7-d688e68fe9a1',
            'from': bot.id,
            'to': user.id,
            'text': 'Gostaria de fazer um teste',
        })
        self.assertEqual(response.status_code, 201)
    
    def test_messages_put(self):
        message = Message.objects.all()[0]
        response = self.client.put(f'/messages/{message.id}/',{
            'from': '?'
        }, content_type='application/json')
        self.assertEqual(response.status_code, 405)

    def test_messages_delete(self):
        message = Message.objects.all()[0]
        response = self.client.delete(f'/messages/{message.id}/')
        self.assertTrue(response.status_code, 405)