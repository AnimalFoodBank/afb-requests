
export interface SessionData {
  id: string
  email: string
  name: string
  role: 'admin' | 'guest' | 'account'
  is_staff: boolean
}
