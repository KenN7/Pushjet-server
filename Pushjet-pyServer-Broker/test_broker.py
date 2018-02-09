import pytest
import broker

def test_brocker(monkeypatch):
    class mocksock():
        def __init__(self,a):
            self.a = a
        
        def recv(self, a):
            print('recv')
            return """{
                "message": {
                        "level": 3,
                        "link": "",
                        "message": "Download just completed",
                        "timestamp": 1410106353,
                        "title": "Cool movie",
                        "service": {
                                "created": 1410106353,
                                "icon": "https://upload.wikimedia.org/wikipedia/commons/8/88/Red_triangle_alert_icon.png",
                                "name": "Important stuff",
                                "public": "4be3-eda97a-0d7faeab05a0-89403-ad4751c49"
                        }
                }
                }"""
        
        def send_string(self, a):
            print('sending')
            raise Exception('Sent')
        
        def bind(self, a):
            pass
        
        def close(self, a):
            raise Exception('Closed')
    
    print('test')
    monkeypatch.setattr('zmq.Context.socket', mocksock)
    with pytest.raises(Exception) as ex:
        broker.main()
    assert 'Sent' in str(ex.value)
