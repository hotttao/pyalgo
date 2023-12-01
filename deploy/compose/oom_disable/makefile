

.PHONY: init
# init env
init:


.PHONY: config
# generate internal proto
config:

.PHONY: api
# generate api proto
api:

.PHONY: build
# build
build:
	docker build . -t memtester:1.0.1

.PHONY: compose
# generate internal proto
compose:
	docker-compose up -d

.PHONY: down
# generate internal proto
down:
	docker-compose down


.PHONY: analysis
# generate internal proto
analysis:
	# docker inspect mem_oom_kill_disable -f '{{.State.Pid}}-{{.State.Status}}-{{.State.OOMKilled}}'
	# docker inspect mem_oom_kill_enable -f '{{.State.Pid}}-{{.State.Status}}-{{.State.OOMKilled}}'  
	docker inspect mem_oom_kill_disable_no_limit -f '{{.State.Pid}}-{{.State.Status}}-{{.State.OOMKilled}}'
	docker inspect mem_50 -f '{{.State.Pid}}-{{.State.Status}}-{{.State.OOMKilled}}'
	docker inspect mem_100 -f '{{.State.Pid}}-{{.State.Status}}-{{.State.OOMKilled}}'
	# docker inspect mem_101 -f '{{.State.Pid}}-{{.State.Status}}-{{.State.OOMKilled}}'
	# docker inspect mem_102 -f '{{.State.Pid}}-{{.State.Status}}-{{.State.OOMKilled}}'

.PHONY: all
# generate all
all:
	make api;
	make config;
	make generate;

# show help
help:
	@echo ''
	@echo 'Usage:'
	@echo ' make [target]'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
	helpMessage = match(lastLine, /^# (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 2, RLENGTH); \
			printf "\033[36m%-22s\033[0m %s\n", helpCommand,helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help
