from flask import Flask, request, jsonify

app=Flask(__name__)

items=[
    {"id":1, "name":"ram", "age":25},
    {"id":2, "name": "rekha", "age": 23}
]

@app.route('/')
def home():
    return "this is home page"

# get method retrive all the items
@app.route("/items", methods=['GET'])
def get_items():
    return jsonify(items)

# get items by id

@app.route("/items/<int:items_id>",methods=['GET'])
def get_items_id(items_id):
    item=next((item for item in items if item['id']==items_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    else:
        return jsonify(item)
    
    
    

# put the items 

@app.route("/items",methods=['POST'])
def create_item():
    if not request.json or not "name" in request.json:
        return jsonify({"Error":"item not in json formate or name key not present "})
    new_items={
        "id" :items[-1]["id"] + 1 if items else 1,
        "name": request.json["name"],
        "age": request.json["age"]
        
    }
    items.append(new_items)
    return jsonify(items)


#put 

@app.route('/items/<int:items_id>',methods=['PUT'])

def update_items(items_id):
    item=next((item for item in items if item['id']==items_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    item["name"]=request.json.get('name', item['name'])
    item['age']=request.json.get('age',item['age'])
    return jsonify(item)

#delete

@app.route('/items/<int:items_id>', methods=['DELETE'])
def delete_items(items_id):
    global item
    item=next((item for item in items if item['id']!=items_id))
    return jsonify({"result":"item deleted"})
    
    



if __name__=='__main__':
    app.run(debug=True)