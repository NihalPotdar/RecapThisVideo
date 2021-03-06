# this is the file where the API is processed
from aiohttp import web
import asyncio
import VideoIntelligence
import SendResults

async def home(request):
    return web.Response(text="Hello World")

async def send_out_results(url, email):
    try:
        # send out the results to the user
        await asyncio.sleep(10)
        #VideoIntelligence.transcribe_video(url)
        Summary = VideoIntelligence.transcribe_video(url)
        
        print(SendResults.formulate_message(email, Summary, url))
    except Exception as e:
        Summary = "There was an error. Please try again."
        
        print(SendResults.formulate_message(email, Summary, url))

async def store_url_and_process_algorithm(request):
    try:
        body = await request.post()

        url = body['url'] # find the url in the request body

        print(url)
        if 'email' in body: # if the user provides an email
            email = body['email']
            print(email)
            asyncio.ensure_future(send_out_results(url, email)) # do it after the current method
            return web.Response(status=200, text="The results will be emailed to you.")

        # doesn't provide email, do it synchronously
        #VideoIntelligence.transcribe_video(url)
        Summary = VideoIntelligence.transcribe_video(url)
        print("Done.")

        return web.Response(status=200, text=Summary)
    except Exception as e:
        print("There's an error: ", e)
        return web.Response(status=400, text="UnSuccessful.") 

# the basic interface of the API
app = web.Application()
app.add_routes([
    web.post('/check_url', store_url_and_process_algorithm),
    web.get('/', home)
])

if __name__ == '__main__':  
    web.run_app(app)