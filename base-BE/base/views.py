from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente
from .serializer import ClienteSerializer
from .models import Transaction
from .serializer import TransactionSerializer

# Show all clients
class showClienteView(APIView):
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Add a new client
class addClienteView(APIView):
    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Cliente agregado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Error al agregar cliente', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Edit an existing client
class editClienteView(APIView):
    def put(self, request, cliente_id):
        try:
            cliente = Cliente.objects.get(id=cliente_id)
            serializer = ClienteSerializer(cliente, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Cliente actualizado correctamente'}, status=status.HTTP_200_OK)
            return Response({'message': 'Error al actualizar cliente', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Cliente.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

# Delete a client
class removeClienteView(APIView):
    def delete(self, request, cliente_id):
        try:
            cliente = Cliente.objects.get(id=cliente_id)
            cliente.delete()
            return Response({'message': 'Cliente eliminado correctamente'}, status=status.HTTP_200_OK)
        except Cliente.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

# Check if a client exists
class checkClienteView(APIView):
    def get(self, request):
        id = request.GET.get('id')
        email = request.GET.get('email')
        client_exists = Cliente.objects.filter(id=id).exists()
        email_exists = Cliente.objects.filter(correo__iexact=email).exists()
        return Response({'idExists': client_exists, 'emailExists': email_exists})


# Show all transactions
class showTransactionView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Add a new transaction
class addTransactionView(APIView):
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Transacción agregada correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Error al agregar transacción', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Edit an existing transaction
class editTransactionView(APIView):
    def put(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            serializer = TransactionSerializer(transaction, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Transacción actualizada correctamente'}, status=status.HTTP_200_OK)
            return Response({'message': 'Error al actualizar transacción', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Transaction.DoesNotExist:
            return Response({'error': 'Transacción no encontrada'}, status=status.HTTP_404_NOT_FOUND)

# Delete a transaction
class removeTransactionView(APIView):
    def delete(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            transaction.delete()
            return Response({'message': 'Transacción eliminada correctamente'}, status=status.HTTP_200_OK)
        except Transaction.DoesNotExist:
            return Response({'error': 'Transacción no encontrada'}, status=status.HTTP_404_NOT_FOUND)

# Check if a transaction exists
class checkTransactionView(APIView):
    def get(self, request):
        id = request.GET.get('id')
        transaction_exists = Transaction.objects.filter(id=id).exists()
        return Response({'idExists': transaction_exists})
