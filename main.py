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

import firebase

timepoint('starting:')


from firebase.cache import printdebug
#import database.cache as cache

import gc
async def main():
	timepoint('init database')
	root=firebase.init()
	timepoint('running test')
	
	root<<{'db':{'testvar':'hello'}}
	await asyncio.sleep(1)
	
	root['db']['testvar2']<<'hello2'
	await printdebug()
	#print(await root())

	#print(test())
	#root['cde']['test2']['hello']<<'haha'
	#print(test())
	#print(test['test']())
	#print(test['test2']())
	#await asyncio.sleep(1)

	
	#await printdebug()
	
	await asyncio.sleep(1)

	#test=None
	await printdebug()


loop=asyncio.get_event_loop()
loop.run_until_complete(main())

timepoint('end:')
