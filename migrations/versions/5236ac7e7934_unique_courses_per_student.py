"""unique courses per student

Revision ID: 5236ac7e7934
Revises: 
Create Date: 2026-10-25 01:28:22.219733

"""
from typing import Sequence, Union
from sqlalchemy import inspect

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5236ac7e7934'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_unique_constraint("uq_student_course", "courses", ["student_id", "title"])
    existing = [i["name"] for i in inspect(op.get_bind()).get_indexes("courses")]
    if "ix_courses_student_id" in existing:
        op.drop_index("ix_courses_student_id", table_name="courses")

def downgrade():
    op.create_index("ix_courses_student_id", "courses", ["student_id"])
    op.drop_constraint("uq_student_course", "courses", type_="unique")