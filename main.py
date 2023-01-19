import streamlit as st
import time
import random

st.set_page_config(page_title="Sort Visual", page_icon=":bar_chart:",
                   layout="wide", initial_sidebar_state="expanded")


def list_to_dict(lista):
    list_dict = []
    for i in range(len(lista)):
        list_dict.append({lista[i]: lista[i]})
    return list_dict


@st.experimental_memo()
def random_list():
    size_list = random.randint(1, 20)
    t = random.sample(range(1, 100), size_list)
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
        "Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Merge Sort 2"))
    slide_speed = st.sidebar.slider("Velocidade", 0.1, 3.0, 1.0, 0.1)

    def manual_list(lista):
        t = [int(i) for i in input_list.split(",")]
        save_list(t)
        return t

    st.title("Sort Visual")
    st.subheader("Algoritmos de ordenação selecionado : " + selection)

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
                    grafico = st.bar_chart(list_to_dict(lista))
                    time.sleep(slide_speed)
                    grafico.empty()
            else:
                if lista[j] < lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    grafico = st.bar_chart(list_to_dict(lista))
                    time.sleep(slide_speed)
                    grafico.empty()
    save_list(lista)


def insertion_sort():
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        if is_crescente:
            while j >= 0 and key < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
        else:
            while j >= 0 and key > lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
        lista[j + 1] = key
        grafico = st.bar_chart(list_to_dict(lista))
        time.sleep(slide_speed)
        grafico.empty()
    save_list(lista)


def selection_sort():
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if is_crescente:
                if lista[min_idx] > lista[j]:
                    min_idx = j
            else:
                if lista[min_idx] < lista[j]:
                    min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        grafico = st.bar_chart(list_to_dict(lista))
        time.sleep(slide_speed)
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
        cp = st.subheader(f"Comparando {L[i]} <= {R[j]}: {L[i] <= R[j]}")
        if L[i] <= R[j]:
            arr[k] = L[i]
            grafico = st.bar_chart(list_to_dict(arr), height=300)
            t = st.subheader(f'Lado esquerdo: {L}   lado direito: {R}' )
            time.sleep(slide_speed)
            t.empty()
            grafico.empty()
            i += 1
        else:
            arr[k] = R[j]
            grafico = st.bar_chart(list_to_dict(arr), height=300)
            t = st.subheader(f'Lado esquerdo: {L}   lado direito: {R}' )
            time.sleep(slide_speed)
            t.empty()
            grafico.empty()
            j += 1
        k += 1
        cp.empty()

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        grafico = st.bar_chart(list_to_dict(arr), height=300)
        t = st.subheader(f'Lado esquerdo: {L}   lado direito: {R}' )
        time.sleep(slide_speed)
        t.empty()
        grafico.empty()
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        grafico = st.bar_chart(list_to_dict(arr), height=300)
        t = st.subheader(f'Lado esquerdo: {L}   lado direito: {R}' )
        time.sleep(slide_speed)
        t.empty()
        grafico.empty()
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
        cp = st.subheader(f"Comparando {L[i]} >= {R[j]}: {L[i] >= R[j]}")
        if L[i] >= R[j]:
            arr[k] = L[i]
            grafico = st.bar_chart(list_to_dict(arr), height=300)
            t = st.subheader(f'Lado esquerdo: {L}   lado direito: {R}' )
            time.sleep(slide_speed)
            t.empty()
            grafico.empty()
            i += 1
        else:
            arr[k] = R[j]
            grafico = st.bar_chart(list_to_dict(arr), height=300)
            t = st.subheader(f'Lado esquerdo: {L}   lado direito: {R}' )
            time.sleep(slide_speed)
            t.empty()
            grafico.empty()
            j += 1
        k += 1
        cp.empty()

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        grafico = st.bar_chart(list_to_dict(arr), height=300)
        t = st.subheader(f'Lado esquerdo: {L}   lado direito: {R}' )
        time.sleep(slide_speed)
        t.empty()
        grafico.empty()
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        grafico

def sort_list():
    if selection == "Bubble Sort":
        bubble_sort()
    if selection == "Insertion Sort":
        insertion_sort()
    if selection == "Selection Sort":
        selection_sort()
    if selection == "Merge Sort":
        arr = load_list()

        def mergesort(A):

            low = 0
            high = len(A) - 1

            temp = A.copy()

            m = 1
            while m <= high - low:

                for i in range(low, high, 2*m):
                    frm = i
                    mid = i + m - 1
                    to = min(i + 2*m - 1, high)
                    if is_crescente: pass
                        # merge_crescente1(A, temp, frm, mid, to, len(temp))
                    else: pass
                        # merge_decrescente1(A, temp, frm, mid, to, len(temp))

                m = 2*m
            save_list(A)
        mergesort(arr)
    if selection == "Merge Sort 2":
        def mergeSort(arr, l, r):
            if l < r:

                # Same as (l+r)//2, but avoids overflow for
                # large l and h
                m = l+(r-l)//2

                # Sort first and second halves
                mergeSort(arr, l, m)
                mergeSort(arr, m+1, r)
                if is_crescente:
                    merge_crescente(arr, l, m, r)
                else:
                    merge_decrescente(arr, l, m, r)
        arr = load_list()
        n = len(arr)
        mergeSort(arr, 0, n-1)
        save_list(arr)


button = st.sidebar.button("Ordenar", on_click=sort_list)
