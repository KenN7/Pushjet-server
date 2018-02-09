#!/usr/bin/python2

import zmq
import argparse
import logging
import json
import signal

parser = argparse.ArgumentParser()
parser.add_argument("-r","--relay", help="relay socket", default="ipc:///tmp/pushjet-relay.ipc")
parser.add_argument("-p","--pub", help="publish socket", default="ipc:///tmp/pushjet-publisher.ipc")

def main():
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Starting up the publishing server')

    context = zmq.Context()
    socketRelay = context.socket(zmq.PULL)
    socketPub = context.socket(zmq.PUB)

    socketRelay.bind(args.relay)
    socketPub.bind(args.pub)

    logging.info("Listening on '%s' and '%s'" % (args.relay, args.pub))

    while(True):
        apiMessageRaw = socketRelay.recv(0)

        logging.info("Parsing message")
        #apiMessage = PushjetApiCall()
        logging.debug('---- \n parsed message :')

        mes = json.loads(apiMessageRaw)
        logging.debug(mes)

        if 'message' in mes:
            if mes['message']['timestamp'] > 0:
                logging.info("Sending out message for %s" % mes['message']['service']['public'])
                socketPub.send_string('%s %s' % (mes['message']['service']['public'],apiMessageRaw))
                #socketPub.Send(fmt.Sprintf("%s %s", apiMessage.Message.Service.Public, apiMessageRaw), 0)

        if 'subscription' in mes:
            if mes['subscription']['timestamp'] > 0:
                logging.info("Sending out subscription update for %s" % mes['subscription']['uuid'])
                socketPub.send_string('%s %s' % (mes['subscription']['uuid'],apiMessageRaw))
                #socketPub.Send(fmt.Sprintf("%s %s", apiMessage.Subscription.Uuid, apiMessageRaw), 0)


    logging.warn('Ending, closing connections!')
    socketRelay.close(args.relay)
    socketPub.close(args.pub)


if __name__ == '__main__':
    main()
