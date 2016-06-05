# coding=utf-8
import sqlalchemy
from sqlalchemy import Column, orm
import sqlalchemy.ext.declarative

Base = sqlalchemy.ext.declarative.declarative_base()

class JobBrief(Base):
    __tablename__ = 'job_brief'

    id = Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    city = Column(sqlalchemy.String(256))
    keyword = Column(sqlalchemy.String(256))

    company_name = Column(sqlalchemy.String(256))
    company_size = Column(sqlalchemy.String(256))
    company_label_list = Column(sqlalchemy.String(256))

    salary_min = Column(sqlalchemy.Float)
    salary_max = Column(sqlalchemy.Float)
    salary_avg = Column(sqlalchemy.Float)

    position_name = Column(sqlalchemy.String(256))
    position_type = Column(sqlalchemy.String(256))
    position_advantage = Column(sqlalchemy.String(256))


class JobDetail(Base):
    __table__ = 'job_detail'

    id = Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    job_id = Column(sqlalchemy.Integer, nullable=False)
    job_bt = Column(sqlalchemy.String(2096), nullable=False, default='')

engine = sqlalchemy.create_engine('sqlite:///data.db')
DBSession = orm.sessionmaker(bind=engine)
