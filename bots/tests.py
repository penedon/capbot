from django.test import TestCase
from django.urls import reverse

from .models import Bot


class BotTestCase(TestCase):
    def setUp(self):
        Bot.objects.create(
            id='36b9f842-ee97-11e8-9443-0242ac120002',
            name='bot'
        )
        Bot.objects.create(
            id='16edd3b3-3f75-40df-af07-2a3813a79ce9',
            name='user'
        )
    
    def test_bot_id_unique(self):
        bot = Bot.objects.get(name='bot')
        unique = bot._meta.get_field('id').unique
        self.assertTrue(unique)

    def test_bot_id_max_length(self):
        bot = Bot.objects.get(name='bot')
        max_length = bot._meta.get_field('id').max_length
        self.assertEquals(max_length, 36)

    def test_bot_get(self):
        response = self.client.get('/bots/')
        self.assertEqual(response.status_code, 200)

    def test_bot_get_id(self):
        response = self.client.get('/bots/36b9f842-ee97-11e8-9443-0242ac120002/')
        self.assertEqual(response.status_code, 200)

    def test_bot_post(self):
        response = self.client.post('/bots/', {
            'id': '16b9f842-ee97-11e8-9443-0242ac120002',
            'name': 'test'
        })
        self.assertEqual(response.status_code, 201)
    
    def test_bot_put(self):
        response = self.client.put('/bots/36b9f842-ee97-11e8-9443-0242ac120002/',{
            'id':'36b9f842-ee97-11e8-9443-0242ac120002',
            'name': 'bot_renamed'
        }, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_bot_delete(self):
        to_delete = Bot.objects.create(
            id='111111111111111111111111111111111',
            name='To Delete'
        )
        response = self.client.delete(f'/bots/{to_delete.id}/')
        self.assertTrue(response.status_code in [200, 204])