#Quick doc for api consumption
#
##
###
####
#####

####################################################
#/app/sign-up/
{
"username": "ray10",
"phone": "0908765456",
"email": "ray10@gmail.com",
"password": "0000"
}

#/app/sign-in/
{
"username": "ray11",
"password": "0000"
}


#/app/verify/
{
"auth_code": "92f7wqv545idyhbwb48skiuh65rehhlf",
"otp_code": "giz0NR"
}


#/app/reset/
{
"auth_code": "92f7wqv545idyhbwb48skiuh65rehhlf",
"password1": "9999",
"password2": "9999"
}

#/app/edit-profile/
{
	"auth_code": "6ydpuz18yzy30d95x0ol1on77d0hwvl0",
	"first_name": "muri",
	"last_name": "ayo",
	"phone": "0908765455"
}

################################################################


#/business/add/
{
"auth_code": "6ydpuz18yzy30d95x0ol1on77d0hwvl0",
"name": "business name",
"business_type": "business type here",
"rc_number": "rc number here",
"category": "business category here",
"location": "business location here",
"description": "description here",
"phone": "business phone here",
"email": "email here",
"website": "website here",
"address": "address here",
"marketplace": "marketplace here",
"marketplace_link": "marketplace link here"
}


#/business/edit/
{
"auth_code": "6ydpuz18yzy30d95x0ol1on77d0hwvl0",
"business_id": "2",
"name": "business name",
"business_type": "business type herexx",
"rc_number": "rc number herexx",
"category": "business category herexx",
"location": "business location herexxx",
"description": "description herexx",
"phone": "business phone herexx",
"email": "email here",
"website": "website here",
"address": "address here",
"marketplace": "marketplace here",
"marketplace_link": "marketplace link here"
}


#/business/delete/
{
"auth_code": "n4v58yp8ttuq83sc5g7vhppgn70kqw1v",
"business_id": "1"
}

#########################################################


#/blog/add/
{
"auth_code": "n4v58yp8ttuq83sc5g7vhppgn70kqw1v",
"business_id": "1",
"title": "blog title",
"detail": "lorem lorem lorem"
}



#/blog/edit/
{
"auth_code": "n4v58yp8ttuq83sc5g7vhppgn70kqw1v",
"blog_id": "1",
"title": "blog title new and changed ",
"detail": "lorem lorem lorem changed lorem"
}


#/blog/delete/
{
"auth_code": "n4v58yp8ttuq83sc5g7vhppgn70kqw1v",
"blog_id": "1"
}
#########################################################


#/product/add/
{
	"auth_code": "6ydpuz18yzy30d95x0ol1on77d0hwvl0",
	"business_id": "1",
	"caption": "product/service caption here",
	"price": "price here",
	"discount": "discount here",
	"color": "color here"
}


#/product/edit/
{
	"auth_code": "6ydpuz18yzy30d95x0ol1on77d0hwvl0",
	"product_id": "1",
	"caption": "product/service caption edit here",
	"price": "price edit here",
	"discount": "discount edit here",
	"color": "color edit here"
}

#/product/delete/
{
	"auth_code": "6ydpuz18yzy30d95x0ol1on77d0hwvl0",
	"product_id": "1"
}

#/blog/add-comment/
{
	"auth_code": "6ydpuz18yzy30d95x0ol1on77d0hwvl0",
	"blog_id": "2",
    "comment": "fuckkkkkk you"
}

#/wishlist/add/
{
	"auth_code": "6ydpuz18yzy30d95x0ol1on77d0hwvl0",
	"product_id": "2"
}
#########################################################

#/app/sign-up/
#/app/sign-in/
#/app/verify/
#/app/reset/
#/app/edit-profile/

#/business/add/
#/business/edit/
#/business/delete/
#/business/get/1/

#/blog/add/
#/blog/edit/
#/blog/delete/
#/blog/add-comment/

#/product/add/
#/product/edit/
#/product/delete/

#/service/add/
#/service/edit/
#/service/delete/

#/review/add/