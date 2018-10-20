FROM php:5.6.26-apache
# Install modules
RUN docker-php-ext-configure mysql --with-mysql=mysqlnd  \
	&& docker-php-ext-install mysql  \
	&& docker-php-ext-configure mysqli --with-mysqli=mysqlnd  \
	&& docker-php-ext-install mysqli  \
	&& docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd  \
	&& docker-php-ext-install pdo_mysql  
	
CMD ["apache2-foreground"]
