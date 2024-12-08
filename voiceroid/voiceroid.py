import clr
 
clr.AddReference('WCFClient')
import AssistantSeika
 
client = AssistantSeika.WCFClient()
 
# 発声
pt = client.Talk(5203, "pythonから呼べましたね", None, None)