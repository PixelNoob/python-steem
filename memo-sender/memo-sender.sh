#!/bin/bash

OLDIFS=$IFS
IFS=","
while read account
    do
    	UNLOCK=<YOUR STEEMPY PASSWORD> steempy transfer --account YOURACCOUNT $account 0.001 "YOUR MEMO HERE"
      sleep 1
done < $1
IFS=$OLIFS
