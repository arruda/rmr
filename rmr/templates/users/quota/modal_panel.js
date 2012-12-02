
{% if request.user.is_authenticated %}	
            $( "#quota-dialog-modal" ).dialog({
                autoOpen: false,
                modal: true,
                buttons: {
                    Ok: function() {                 
                        var new_form = $("#quota-dl-form");
						
						var post_url = '{% url ajax_change_quota %}';

                        $.post(post_url,
                            new_form.serialize(),
                            function(data) {
                            	if(data.errors !== undefined){
					                //for each field in the errrors
				                    $.each(data.errors, function(key, value) { 
				                       	var field = new_form;
			
				                       	//if it's not a general error, than add it to the expecific field
				                       	//else just add it to the form
				                    	if(key != "__all__"){
				                       		var field = new_form.find("[name='" + key + "']").parent();
				                    	}
			
				                        //add each error to the given field
				                        $.each(value, function(index, val){
				                           field.prepend("<span class='error'>"+val+"</span>");
			
				                        });
				                    });
			                    }
                            	else{
	                                console.log(data);
	
                                    
	
	                                $( "#quota-dialog-modal" ).dialog( "close" );

                                    location.reload();
	                                
                            	}

                            },"json");
                

                    },
                    Cancel: function() {
                        $( this ).dialog( "close" );
                    }
                },
                close: function() {                   
                    $( this ).dialog( "close" );
                    var new_form = $( this ).find("#quota-dl-form");

                    new_form.find("input").val("{{request.user.get_profile.quota|stringformat:".2f"}}");
                    new_form.find(".error").remove();   
                    console.log("close");
                }
            });
	
		
                
            //change the add buttons to do what it must
            $('#change_quota').click(function(){
                event.preventDefault();
                
                var dialog = $( "#quota-dialog-modal" );
                console.log("change_quota");          
                      
                dialog.dialog( "open" );    
            });

{% endif %}
