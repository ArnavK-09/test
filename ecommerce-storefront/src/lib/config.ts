import Medusa from "@medusajs/medusa-js"
import { QueryClient } from "@tanstack/react-query"

// Defaults to standard port for Medusa server
let MEDUSA_BACKEND_URL = "https://studious-trout-46659j5jvjv2jqr5-9000.app.github.dev"

// if (process.env.NEXT_PUBLIC_MEDUSA_BACKEND_URL) {
//   MEDUSA_BACKEND_URL = process.env.NEXT_PUBLIC_MEDUSA_BACKEND_URL
// }

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      staleTime: 1000 * 60 * 60 * 24,
      retry: 1,
    },
  },
})

const medusaClient = new Medusa({ baseUrl: MEDUSA_BACKEND_URL, maxRetries: 3, publishableApiKey: 'c2NyeXB0AAEAAAABAAAAASIIiBayH3a18k2AR4ooVQ/eRxq9/WMb/01tu4kZWjXBjKzaNrnFWsClCmA5Yw4WTdrnKkoZ6EvLnKPEPRkrxivyb+CES3wdh5T0w97PF9jR' })

export { MEDUSA_BACKEND_URL, queryClient, medusaClient }
