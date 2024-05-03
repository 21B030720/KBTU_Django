import dramatiq

from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend

from logic import crime_service, psycho_service, drugs_service

from db import db

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)


@dramatiq.actor(store_results=True)
def add_employee_task(iin: str):
    print('started')
    # db.append(iin)
    result = crime_service(iin) & drugs_service(iin) & psycho_service(iin)
    print('ended', result)
    return result