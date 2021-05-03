from flask import escape

def hello_http(request):

"""HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
"""
     
    request_json = request.get_json(silent=True) #create a json request variable
    request_args = request.args #create a argument request variable
    
    if request_json and 'file' in request_json:
        file_name = request_json['file'] #file_name stores the name of the input file
        
    myfile = open(file_name, "rt")
    val = myfile.readline()
    val = val[:-1] #remove the '\n' newline character from the line                         
    input_dict = json.loads(val) #stores the dictionary from the input file
    
    ls = list(input_dict['a']+input_dict['b']) #combine the 2 array and elements convert the type into list
    ls.sort()
    return ls #To print within the same function: print(*ls)

"""
type the below command in the cloud shell:

curl -X POST HTTP_TRIGGER_ENDPOINT -H "Content-Type:application/json"  -d '{"file":"input.py"}'

Here, HTTP_TRIGGER_ENDPOINT is the URL for the function, obtained when the function is deployed. 
"""
