# -*- coding:utf-8 -*-

start_button = """<button class ="btn btn-success"
                onclick= "$.get(%s, function(){alert('start spidering...');});" >start</button>"""

result_url = "'result?platform_name=%s&spider_id=%s&db_host=%s&db_name=%s&db_user=%s'"


result_button = """<button class ="btn btn-success" onclick= 
                "window.open(%s)" >watch</button>"""


# result_button = """<button class ="btn btn-success" onclick= "(function(){
#                                                                         $.get(%s);
#                                                                         window.open('/result_page');
#                                                                         })()" >watch</button>"""


