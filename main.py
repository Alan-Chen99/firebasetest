#TODO: change secret

#env vars:

#FIREBASE_CONFIG
#{
#	"databaseURL":
#	"https://databaseName.firebaseio.com"
#}

#GOOGLE_APPLICATION_CREDENTIALS
#from console.firebase.google.com
from utils.timing import timepoint
timepoint('imports:')

#from utils.task import sync_ensure
#from utils.task import addtask

import asyncio

timepoint('importing database:')

import database

timepoint('starting:')


from database.cache import printdebug
#import database.cache as cache

import gc
async def main():
	timepoint('init database')
	root=database.init()

	timepoint('running test')
	
	tmproot=root
	root=tmproot['tmp']
	root<<None

	#await printdebug()

	root['abc']<<'test2'

	#await asyncio.sleep(1)
	#await printdebug()
	#test=
	root['cde']<<{'testbefore':'beforeval'}
	#await asyncio.sleep(1)
	
	#print(test())

	#await printdebug()

	root<<{'cde':{'test':'cdeval'},'abc':'abcval'}
	#await asyncio.sleep(1)
#gc.collect()
	#print(cache.pending)
	
	#await printdebug()

	print(await root['cde']())
	
	#print(test())
	#root['cde']['test2']['hello']<<'haha'
	#print(test())
	#print(test['test']())
	#print(test['test2']())
	#await asyncio.sleep(1)

	
	await asyncio.sleep(1)
	#await printdebug()
	
	await asyncio.sleep(1)

	test=None
	await printdebug()


loop=asyncio.get_event_loop()
loop.run_until_complete(main())

timepoint('end:')
