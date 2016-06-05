# coding=utf-8
import pymongo
from pymongo.collection import Collection
from pymongo.database import Database

import config

def get_mongo_client(host='', port=''):
    """

    :param host:
    :param port:
    :return:
    :rtype: pymongo.MongoClient
    """

    host = host if host else config.MONGODB_HOST
    port = port if port else config.MONGODB_PORT

    client = pymongo.MongoClient(host, port)

    return client

def get_lagou_db(client):
    """

    :param client:
    :type client: pymongo.MongoClient
    :return:
    :rtype: Database
    """

    return client[config.MONGODB_NAME]


def get_job_brief_collection(db):
    """

    :param client:
    :type db: Database
    :return:
    :rtype: Collection
    """

    return db[config.MONGODB_COLLECTION_BRIEF]

def get_job_detail_collection(db):
    """

    :param db:
    :type db: Database
    :return:
    :rtype: Collection
    """

    return db[config.MONGODB_COLLECTION_DETAIL]