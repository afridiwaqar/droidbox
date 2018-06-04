#!/usr/bin/env bash

emulator -avd Android412 -system images/system.img -ramdisk images/ramdisk.img -wipe-data -prop dalvik.vm.execution-mode=int:portable &
