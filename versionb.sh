file=$1
basename=$(echo $file | tr "." " " )
d=$(date +'%Y-%m-%d')
touch  "$basename"_"d".txt

