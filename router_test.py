import streamlit as st
import extra_streamlit_components as stx


# @st.cache_dat(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def init_router():
    return stx.Router({"/home": home, "/landing": landing})

def home():
    return st.write("This is a home page")

def landing():
    return st.write("This is the landing page")

router = init_router()
router.show_route_view()

c1, c2, c3 = st.columns(3)

with c1:
    st.header("Current route")
    current_route = router.get_url_route()
    st.write(f"{current_route}")
with c2:
    st.header("Set route")
    new_route = st.text_input("route")
    if st.button("Route now!"):
        router.route(new_route)
with c3:
    st.header("Session state")
    st.write(st.session_state)