 function getAllAjax(callback){
        $.ajax({
            "url": "datacollections/",
            "method":"GET",
            "data":"",
            "dataType": "JSON",
            "success":function(result){
                //console.log(result);
                add
                callback(result)
     
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }

    // testing code
    function createCollection(collection, callback){
        console.log(JSON.stringify(collection));
        $.ajax({
            "url": "datacollections/",
            "method":"POST",
            "data":JSON.stringify(collection),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                //console.log(result);
                callback(result)  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }
    function updateCollection(collection, callback){
        console.log("updateing " +JSON.stringify(collection));
        $.ajax({
            "url": "datacollections/"+encodeURI(collection.id),
            "method":"PUT",
            "data":JSON.stringify(collection),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log(result);
                callback(result)   
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }
    function deleteCollection(id, callback){
        $.ajax({
            "url": "datacollections/"+id,
            "method":"DELETE",
            "data":"",
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log(result);
                callback(result)  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }



    // testing code
    
    function processGetAllResponse(result){
        console.log("in process")
        //console.log(result)
        for (collection of result){
            //console.log(collection)
            // or convert
            displayCollection = {}
            displayCollection.id = collection.id
            displayCollection.name = collection.name
            displayCollection.collectiontype = collectioncollectiontype
            displayCollection.startdate = collection.startdate
            displayCollection.enddate = collection.enddate
            displayCollection.location = collection.location
            displayCollection.measurement = collection.measurement
            displayCollection.units = collection.units

            console.log(displayCollection)
        }
    }
     getAll(processGetAllResponse)

     ///// Create
    function processCreateResponse(result){
        console.log(result)
    }

    //// update
    function processUpdateResponse(result){
        console.log(result)
    }
    
    function processDeleteResponse(result){
        console.log("in pprocess delete")
        console.log(result)
    }
