"""DML

Revision ID: 3b9ffdecb9d0
Revises: 61731cc61adf
Create Date: 2020-03-07 00:05:48.280856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b9ffdecb9d0'
down_revision = '61731cc61adf'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    INSERT INTO person(
        first_name, middle_name, last_name, date_of_birth, gender, national_identifier)
        VALUES ('Jack', 'Thomas', 'Edisson', '20-MAY-1996', 'M', '1110-22-1');
        
    INSERT INTO person(
        first_name, middle_name, last_name, date_of_birth, gender, national_identifier)
        VALUES ('Max', 'Pane', 'Tres', '28-JAN-2000', 'M', '3310-99-0');
    
    
    INSERT INTO address(
        line_1, line_2, state, country, zip_code, person_id)
        VALUES ('street 23', 'house 34', 'MS', 'UA', '78500', 1);
    
    INSERT INTO address(
        line_1, line_2, state, country, zip_code, person_id)
        VALUES ('street 23', 'house 35', 'MS', 'UA', '78500', 1);
    
    INSERT INTO address(
        line_1, line_2, state, country, zip_code, person_id)
        VALUES ('street 3', 'house 31', 'MA', 'UA', '78500', 2);

    """)


def downgrade():
    op.execute("""
    DELETE FROM ADDRESS;
    DELETE FROM PERSON;
    SELECT pg_catalog.setval('public.person_id_seq', 1, false);
    SELECT pg_catalog.setval('public.address_id_seq', 1, false);
    """)