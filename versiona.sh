file=$1
datetoday=$(date +'%Y-%m-%d')
if [ -e $file ]
then 
	echo file exist and copied
	cp $file "$datetoday"_"$file"
else
	echo new file created
	touch "$datetoday"_"$file"
fi
