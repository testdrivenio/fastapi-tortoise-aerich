from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Event(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    class Meta:
        table = "event"

    def __str__(self):
        return self.name


EventSchema = pydantic_model_creator(Event)
