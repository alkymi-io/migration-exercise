# Migration Exercise

This repository contains a boilerplate Django project with a set of models
and migrations in the `store` app.

## Task

Implement the `RunPython` migration in `store/migrations/0002_cell_field.py`.

Given a `Cell` object `cell`, the migration should set the value of
`cell.field` by finding a matching `Field` object where:

- `cell.field_name == field.name` and
- `cell.record.schema == field.schema`.

## Performance Considerations

Assume the following data properties:

- The database has tens of millions of Cell objects,
- millions of records,
- hundreds of fields,
- tens of schemas.
