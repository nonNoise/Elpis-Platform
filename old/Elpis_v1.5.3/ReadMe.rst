========================================================
Elpis v1.5　開発メモ
========================================================



Supervisor　の設定
-----------------------------

> sudo pip install supervisor

> sudo sh -c "echo_supervisord_conf > /etc/supervisor/supervisord.conf"

> sudo supervisord -c /home/kitagami/Github/Elpis/v1.5/config/supervisor/supervisord.conf

unix:///var/run/supervisor.sock refused connection
が出た際は、指定のファイルを削除の後、再チャレンジ


