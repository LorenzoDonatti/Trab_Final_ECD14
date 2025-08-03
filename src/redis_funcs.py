import aioredis

redis_instance = None

async def dependency_redis():

    global redis_instance
    return redis_instance


async def startup_event():

    global redis_instance
    redis_instance = await aioredis.from_url("redis://redis:6379")


async def shutdown_event():

    global redis_instance
    await redis_instance.close()