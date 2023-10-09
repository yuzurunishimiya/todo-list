from marshmallow import Schema, fields


class TaskAdd(Schema):
    """request JSON of add task"""

    task = fields.String(required=True)
    status_id = fields.Int(strict=True)
    priority_id = fields.Int(strict=False)
    start_date_time = fields.Str(required=False, default=None)
    end_date_time = fields.Str(required=False, default=None)
