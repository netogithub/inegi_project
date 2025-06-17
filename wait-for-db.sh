#!/bin/sh
# set -e

# timeout=30
# echo "Esperando a que MySQL esté listo..."
# while ! mysqladmin ping -h"$DB_HOST" -u"$DB_USER" -p"$DB_PASSWORD" --silent; do
#   timeout=$((timeout - 1))
#   if [ $timeout -eq 0 ]; then
#     echo "MySQL no está listo después de $timeout segundos"
#     exit 1
#   fi
#   sleep 1
# done
# echo "MySQL está listo!"

#!/bin/sh
# wait-for-db.sh

set -e

host="$1"
shift
cmd="$@"

until mysqladmin ping -h"$host" -u"root" -p"${DB_ROOT_PASSWORD}" --silent; do
  >&2 echo "MySQL no está listo. Reintentando..."
  sleep 1
done

>&2 echo "MySQL está listo. Ejecutando comando..."
exec $cmd