from pythonosc import osc_message_builder
from pythonosc import udp_client

#Setting up a client
client = udp_client.SimpleUDPClient('127.0.0.1', 57110)


def oscgrain( frequency ):
    """ 
    The synthdefs in the Supercollider-server on localhost is receving OSC messages via port 57110 in the following way:
    "s_new", \nameofsynthdef, -1, 0, 1, \argument_1, argumenvalue_1 (as int or float), \argument_2, argumenvalue_2, ... \argument_n, argumenvalue_n
    The values (-1, 0, 1) between \nameofsynthdef and \argument_1 are explained here in detail. The procedure to send was named "oscgrain" and defined as a function.
    """
    msg = osc_message_builder.OscMessageBuilder(address = "s_new")
    msg.add_arg("grain")
    msg.add_arg(-1)
    msg.add_arg(0)
    msg.add_arg(1)
    msg.add_arg("amp")
    msg.add_arg(1)
    msg.add_arg("freq")
    msg.add_arg(frequency)
    msg.add_arg("sustain")
    msg.add_arg(0.01) #0.01-0.04
    msg.add_arg("pan")
    msg.add_arg(0)
    msg = msg.build()
    client.send(msg) 