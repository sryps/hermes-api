# API for hermes queries

Make sure to update config.toml for hermes.

```
...
rpc_addr = 'http://localhost:26440'
grpc_addr = 'http://localhost:26442'
```

Add all chains you wish to query. For more info on hermes config visit: https://hermes.informal.systems

Dockerfile included.

`http://localhost:5000/hermes?chain=osmosis-1&channel=channel-0`