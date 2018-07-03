while true
do
    if [ -f "./CALC" ] && [ ! -f "./DONE" ]
    then
        echo "go"
        rm "./CALC"
        define < tst.def
        ridft
        t2x -c > final.xyz
        touch "./DONE"
    else
        echo "no"
    fi
    sleep 1
done