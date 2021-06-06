#TODO: change secret

#secrets:

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




async def main():
	timepoint('init database')
	root=database.init()

	timepoint('running test')
	
	root<<None

	root['abc']<<'test2'

	test=root['cde']<<{'testbefore':'beforeval'}
	print(test())
	root<<{'cde':{'test':'cdeval'},'abc':'abcval'}
	print(test())
	root['cde']['test2']['hello']<<'haha'
	print(test())
	print(test['test']())
	print(test['test2']())
	await asyncio.sleep(1)
	#root.delete()
	#await baseget('a')


	#timepoint('starting test')

	#asyncio.gather(*[coro("group 1.{}".format(i)) for i in range(1, 6)])

	#timepoint('timing 100 get operations in a sequence:')
	#tmp=asyncio.gather(*[baseget(f'{i}') for i in range(100)])
	#await tmp
	
	#timepoint('end test')
	#await asyncio.sleep(1)
	#print(root)
	#a=root['a']['b']['c']
	#b=root['a']['x']['c']
	#for x in a.ancestorswithself():
	#	print(x.path)
	#print(b.path)
	#await cache.init()
	
	
	#await basedb.baseupdate({'abc/':'teststr'})
	#await asyncio.sleep(5)
	#await basedb.baseupdate({'abc/def/':{'hello':1.2}})
	#test=await basedb.baseget('abc/')
	#print(test)


loop=asyncio.get_event_loop()
loop.run_until_complete(main())

timepoint('end:')
