from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Category
from app1.models import Product
from app1.models import SalesOrder
import json

# Create your views here.

############ Category #############
class CategoryAPIView(APIView):

    #########Post(insert)###########
	def post(self,request):
		data = request.data
		try:
			cat = Category(name=data.get('name'))
			cat.save()
			message="Category %s inserted successfully" % cat.name
			#raise Exception('Category not Created.')
			status_code = 200
		except Exception as err:
			message = str(err)
			status_code=400	
		return Response({"message":message},status= status_code)


    ##########get method########
	def get(self,request,cat_id=None):
		items = []
		cats = []
		status_code=200
		data = {"message":"Success","items":items}
		if cat_id:
			try:
				cats = Category.objects.get(id=cat_id)
				if cats:
					cats = [cats]
			except Exception as err:
				data['message']=str(err)
				status_code=404

		else:
			cats = Category.objects.all()
		for cat in cats:
			items.append({"name":cat.name})
		return Response(data,status=status_code)	

    ###########PUT (update)###########
	def put(self,request,cat_id):
		data = {"message":"Success"}
		status_code = 200
		try:
			cat = Category.objects.get(id=cat_id)
			request_data = request.data
			cat.name = request_data.get("name")
			cat.save()
		except Exception as err:
			data['message'] = str(err)
			status_code = 404
		return Response(data,status=status_code)
     ############Delete##########
	def delete(self,request,cat_id):
		data = {"message":"Delete successfully"}
		status_code = 200
		try:
			cat = Category.objects.get(id=cat_id)
			cat.delete()
		except Exception as err:
			data['message'] = str(err)
			status_code = 404
		return Response(data,status=status_code)

################### PRODUCT ###################
class ProductAPIView(APIView):

	##########Post method########
	def post(self,request):
		data = request.data

		try:
			cat = Category.objects.get(id=2)
			pro = Product(name=data.get('name'),cost=data.get('cost'),category=cat)
			pro.save()
			message="Product %s%s inserted successfully" % pro.name,pro.cost,pro.category
			#raise Exception('Category not Created.')
			status_code = 200
		except Exception as err:
			message = str(err)
			status_code=400	
		return Response({"message":message},status= status_code)

    ##########get method########
	def get(self,request,pro_id=None):
		items = []
		pros = []
		status_code=200
		data = {"message":"Success","items":items}
		if pro_id:
			try:
				pros = Product.objects.get(id=pro_id)
				if pros:
					pros = [pros]
			except Exception as err:
				data['message']=str(err)
				status_code=404

		else:
			pros = Product.objects.all()
		for cat in pros:
			items.append({"name":cat.name})
		return Response(data,status=status_code)		

     #################PUT (update)###############
	def put(self,request,pro_id):
		data = {"message":"Success"}
		status_code = 200
		try:
			pro = Product.objects.get(id=pro_id)
			request_data = request.data
			pro.name = request_data.get("name")
			pro.save()
		except Exception as err:
			data['message'] = str(err)
			status_code = 404
		return Response(data,status=status_code)

     ############Delete##########
	def delete(self,request,pro_id):
		data = {"message":"Delete successfully!!!!"}
		status_code = 200
		try:
			pro = Product.objects.get(id=pro_id)
			pro.delete()
		except Exception as err:
			data['message'] = str(err)
			status_code = 404
		return Response(data,status=status_code)



############## SalesOrder #############

class SalesAPIView(APIView):

	##########Post method########
	def post(self,request):
		data = request.data
		try:
			sale = SalesOrder(description=data.get('description'))
			sale.save()

			for prod_id in data.get("products"):	
				prod = Product.objects.get(id=prod_id)
				sale.products.add(prod)
				
			message="SalesOrder %s inserted successfully" % sale.description
			#raise Exception('Category not Created.')
			status_code = 200
		except Exception as err:
			message = str(err)
			status_code=400	
		return Response({"message":message},status= status_code)
	 ##########get method########
	def get(self,request,sal_id=None):
		items = []
		sales = []
		status_code=200
		data = {"message":"Success","items":items}
		if sal_id:
			try:
				sales = SalesOrder.objects.get(id=sal_id)
				if sales:
					sales = [sales]
			except Exception as err:
				data['message']=str(err)
				status_code=404

		else:
			sales = SalesOrder.objects.all()
		for cat in sales:
			items.append({"description":cat.description})
		return Response(data,status=status_code)	

	 #################PUT (update)###############
	def put(self,request,sal_id):
		data = {"message":"Success"}
		status_code = 200
		try:
			sale = SalesOrder.objects.get(id=sal_id)
			request_data = request.data
			sale.description = request_data.get("description")
			sale.save()
		except Exception as err:
			data['message'] = str(err)
			status_code = 404
		return Response(data,status=status_code)
	

	 ############Delete##########
	def delete(self,request,sal_id):
		data = {"message":"Delete successfully!!!!"}
		status_code = 200
		try:
			sale = SalesOrder.objects.get(id=sal_id)
			sale.delete()
		except Exception as err:
			data['message'] = str(err)
			status_code = 404
		return Response(data,status=status_code)	






