#! /bin/bash
echo "==================================================="
echo "Dockerfile을 build합니다."
echo "==================================================="
 docker build --build-arg DEPENDENCY=build/dependency -t hcs4125/sendwish_scrapping --platform linux/amd64 .
echo "done."

echo "==================================================="
echo "Dockerfile을 push합니다." 
echo "==================================================="
docker push hcs4125/sendwish_scrapping
echo "done."
