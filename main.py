import subprocess
from datetime import datetime, timezone
from get_time import display_time

dir = "~/github/hermes-api/config.toml"

def getClient(homeDir, chain, channel) :
    cmd = "hermes --config "+homeDir+" --json query channel client --chain "+chain+" --port transfer  --channel " + channel +" | jq -r .result.client_id"
    capture = subprocess.run(cmd,capture_output=True,shell=True)
    return  capture.stdout.decode('utf-8').lstrip('null\n').rstrip('\n')

def getHeight(homeDir, chain, clientId) :
    cmd = "hermes --config "+homeDir+" --json query client consensus --chain "+chain+" --client " + clientId + " | jq '.result | last | .revision_height'"
    capture = subprocess.run(cmd,capture_output=True,shell=True)
    return  capture.stdout.decode('utf-8').lstrip('null\n').rstrip('\n')

def getTimestamp(homeDir, chainId, clientId, consensusHeight) :
    cmd = "hermes --config "+homeDir+" --json query client consensus --chain "+chainId+" --client "+clientId+" --consensus-height "+consensusHeight+" | jq -r .result.timestamp"
    capture = subprocess.run(cmd,capture_output=True,shell=True)
    return  capture.stdout.decode('utf-8').lstrip('null\n').rstrip('\n')


def checkTimestamp(t) :
    now = datetime.now(tz=timezone.utc).timestamp()
    timestamp_string = t.replace("T", "-").replace("Z","").split(".", 1)[0]
    format_string = "%Y-%m-%d-%H:%M:%S"
    timestamp = datetime.strptime(timestamp_string,format_string).timestamp()
    diff = now - timestamp
    resp = display_time(diff)
    return resp


chain = "osmosis-1"
channel = "channel-47"
client = getClient(dir, chain, channel)

height = getHeight(dir, chain, client)

time = getTimestamp(dir, chain, client, height)

check = checkTimestamp(time)
ret = {}
ret['chain_id'] = chain
ret['channel_id'] = channel
ret['block_height'] = height
ret['client_id'] = client
ret['time_since_last_update'] = check
print(ret)
