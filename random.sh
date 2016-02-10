path="/usr/share/dict/words"
words=$path
ran="$RANDOM"
echo $(sed -n "$ran p" $words)
