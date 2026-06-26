<script setup>
import { ref } from 'vue'

const props = defineProps({
  src: {
    type: String,
    required: true
  },
  class: {
    type: String,
    default: ''
  }
})

const isOpen = ref(false)

function toggle() {
  isOpen.value = !isOpen.value
  if (isOpen.value) {
    document.body.style.overflow = 'hidden'
  } else {
    document.body.style.overflow = ''
  }
}
</script>

<template>
  <div class="cursor-zoom-in" @click="toggle">
    <!-- Miniatura -->
    <img :src="src" :class="props.class" />

    <!-- Overlay Pantalla Completa -->
    <Teleport to="body">
      <div 
        v-if="isOpen" 
        class="fixed inset-0 bg-black/90 z-[999] flex items-center justify-center cursor-zoom-out animate-fade-in"
        @click="toggle"
      >
        <img 
          :src="src" 
          class="max-w-full max-h-full object-contain shadow-2xl transition-transform duration-300 scale-100"
        />
      </div>
    </Teleport>
  </div>
</template>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.2s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}
</style>
