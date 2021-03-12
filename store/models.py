from django.db import models


class Record(models.Model):
    schema = models.ForeignKey('store.Schema',
                               on_delete=models.CASCADE)


class Cell(models.Model):
    record = models.ForeignKey('store.Record',
                               on_delete=models.CASCADE)
    field_name = models.TextField()

    field = models.ForeignKey('store.Field',
                              null=True,
                              on_delete=models.CASCADE)
    """Newly added ForeignKey.

    This field is new. We want to write a migration that sets
    ``field`` by finding a Field with a matching ``name`` to
    the cell's ``field_name``.

    """

class Schema(models.Model):
    name = models.TextField()


class Field(models.Model):
    name = models.TextField()
    schema = models.ForeignKey(
        'store.Schema', on_delete=models.CASCADE)
