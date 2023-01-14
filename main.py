import streamlit as st
import time
import random

st.set_page_config(page_title="Sort Visual", page_icon=":bar_chart:",
                   layout="wide", initial_sidebar_state="expanded")


@st.experimental_memo()
def random_list():
    size_list = random.randint(1, 20)
    t = random.sample(range(1, 100), size_list)
    print(len(t))
    if len(t) <= 5:
       return random_list()
    save_list(t)


def list_to_str(lista):
    return ",".join([str(i) for i in lista])


def manual_list():
    return [int(i) for i in input_list.split(",")]


def str_to_list(lista):
    return [int(i) for i in lista.split(",")]


def remove_cache():
    random_list.clear()


def save_list(lista):
    with open("save_state.txt", "w") as file:
        file.write(list_to_str(lista))


def load_list():
    with open("save_state.txt", "r") as file:
        lista = file.read()
        lista = str_to_list(lista)
        return lista


def save_list(lista):
    with open("save_state.txt", "w") as file:
        file.write(list_to_str(lista))


def load_list():
    with open("save_state.txt", "r") as file:
        lista = file.read()
        lista = str_to_list(lista)
        return lista


def resert_list():
    with open("save_state.txt", "w") as file:
        file.write("1,2,3,4,5,6,7,8")


try:
    insecao = st.sidebar.selectbox(
        "Maneira de inserção", ("Aleatório", "Manual"), on_change=remove_cache)
    button_random = st.sidebar.button(
        "Gerar lista aleatória", on_click=remove_cache, disabled=(insecao == 'Manual'))
    input_list = st.sidebar.text_input("Digite os números separados por vírgula", list_to_str(
        load_list()), disabled=(insecao == 'Aleatório'))
    reverse = st.sidebar.radio("Ordem", ("Crescente", "Decrescente"))
    selection = st.sidebar.selectbox("Selecione o algoritmo", (
        "Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Quick Sort"))

    def manual_list(lista):
        t = [int(i) for i in input_list.split(",")]
        save_list(t)
        return t

    if insecao == "Aleatório":
        lista = random_list()
        lista = load_list()
    if insecao == "Manual":
        lista = manual_list(input_list)

    if reverse == "Decrescente":
        is_crescente = False
    if reverse == "Crescente":
        is_crescente = True

    show_list = st.text(lista)
    grafico = st.bar_chart(load_list())
    if load_list() == []:
        st.error("Lista vazia")
        random_list()

except:
    st.error("Lista vazia")
    button_reset = st.sidebar.button("Resetar app", on_click=resert_list)


def bubble_sort():
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if is_crescente:
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    grafico = st.bar_chart(lista)
                    time.sleep(1)
                    grafico.empty()
            else:
                if lista[j] < lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    grafico = st.bar_chart(lista)
                    time.sleep(1)
                    grafico.empty()
    save_list(lista)


def insertion_sort():
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
        grafico = st.bar_chart(lista)
        time.sleep(1)
        grafico.empty()
    save_list(lista)


def selection_sort():
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[min_idx] > lista[j]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        grafico = st.bar_chart(lista)
        time.sleep(1)
        grafico.empty()
    save_list(lista)


def merge_crescente(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_decrescente(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] >= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
# l is for left index and r is right index of the
# sub-array of arr to be sorted


def sort_list():
    if selection == "Bubble Sort":
        bubble_sort()
    if selection == "Insertion Sort":
        insertion_sort()
    if selection == "Selection Sort":
        selection_sort()
    if selection == "Merge Sort":
        arr = load_list()

        def mergeSort(arr, l, r, reverse=False):
            if l < r:

                # Same as (l+r)//2, but avoids overflow for
                # large l and h
                m = l+(r-l)//2

                # Sort first and second halves
                mergeSort(arr, l, m, reverse)

                mergeSort(arr, m+1, r, reverse)
                if reverse:
                    merge_decrescente(arr, l, m, r)
                else:
                    merge_crescente(arr, l, m, r)

                grafico = st.bar_chart(arr)
                time.sleep(1)
                grafico.empty()
                save_list(arr)

        n = len(arr)
        mergeSort(arr, 0, n-1, reverse=is_crescente)


button = st.sidebar.button("Ordenar", on_click=sort_list)
