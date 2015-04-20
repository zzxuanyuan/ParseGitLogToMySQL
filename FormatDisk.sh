#!/bin/bash
for i in 1 2 3; do
	mkdir -p /srv/node/d$i
	mount -t xfs -L d$i /srv/node/d$i
done
