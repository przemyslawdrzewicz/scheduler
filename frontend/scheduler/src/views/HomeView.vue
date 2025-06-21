<script setup lang="ts">
import { onMounted } from 'vue'

onMounted(async () => {
  const response = await fetch('http://localhost:8000/calendar/')
})
</script>

<template>
  <main>hello</main>
</template>
