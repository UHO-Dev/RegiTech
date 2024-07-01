function borrarModal(){
    window.open("{% url 'RecursoDelete' recurso.id %}", "_blank", "width=600,height=400");
}
