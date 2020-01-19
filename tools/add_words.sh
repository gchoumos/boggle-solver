cat new_words.xml | grep "class=\"word\"" | cut -d'>' -f2 | cut -d'<' -f1 | sort -u | awk {'print toupper($_)'} > app1
ll
cat app1 backup | sort -u > gr_dict_uniq 
wc -l greek
wc -l gr_dict_uniq 
cp gr_dict_uniq greek
cp gr_dict_uniq backup 
wc -l backup