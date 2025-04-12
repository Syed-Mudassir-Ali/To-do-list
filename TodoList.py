import streamlit as st

# Session state me tasks store karo
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("📝 To-Do List App")

# --- Add Task ---
new_task = st.text_input("Enter a new task:")
if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success("✅ Task added!")

# --- View and Update Tasks ---
if st.session_state.tasks:
    st.subheader("📋 Your Tasks")

    for i, t in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([6, 2, 2])
        
        with col1:
            st.write(f"{i+1}. {t['task']}")

        with col2:
            if not t["done"] and st.button(f"✔️ Done", key=f"done_{i}"):
                st.session_state.tasks[i]["done"] = True

        with col3:
            if st.button(f"🗑️ Delete", key=f"del_{i}"):
                st.session_state.tasks.pop(i)
                st.experimental_rerun()

        if t["done"]:
            st.markdown(f"<span style='color:green;'>Status: ✔️ Done</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<span style='color:red;'>Status: ❌ Not Done</span>", unsafe_allow_html=True)
else:
    st.info("📭 No tasks yet.")
