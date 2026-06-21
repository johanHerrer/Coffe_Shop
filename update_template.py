content = '''<div
class="bg-white dark:bg-[#1E1E1E] rounded-3xl overflow-hidden shadow-lg hover:shadow-2xl transition duration-500 hover:-translate-y-2">

    <!-- IMAGE -->
    <div class="h-64 overflow-hidden">

        <img
        src="/media/{{ product.image }}"
        class="w-full h-full object-cover hover:scale-110 transition duration-700">

    </div>

    <!-- CONTENT -->
    <div class="p-6">

        <div class="flex justify-between items-center">

            <h2 class="text-2xl font-bold">
                {{ product.name }}
            </h2>

            <span
            class="bg-[#6F4E37] text-white px-4 py-1 rounded-full">

                ${{ product.price }}

            </span>

        </div>

        <p class="mt-4 text-gray-600 dark:text-gray-400">

            {{ product.description|truncatechars:80 }}

        </p>

        <div class="flex justify-between items-center mt-6">

            <span class="text-sm text-gray-500">

                Stock: {{ product.stock }}

            </span>

            <div class="flex gap-2">

                <a
                href="{% url 'add_to_cart' product.id %}"
                class="bg-[#6F4E37] text-white px-4 py-2 rounded-xl hover:scale-105 transition">

                    Agregar

                </a>

                {% if request.session.user_role == 'admin' %}
                    <a
                    href="{% url 'delete_product' product.id %}"
                    class="bg-red-500 text-white px-4 py-2 rounded-xl hover:scale-105 transition">

                        Eliminar

                    </a>
                {% endif %}

            </div>

        </div>

    </div>

</div>'''

with open(r'c:\Users\herre\Desktop\WorkSpace\coffee_shop\templates\products\components\product_card.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated product_card.html')
