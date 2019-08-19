package hello

import io.ktor.application.*
import io.ktor.http.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*

fun main(args: Array<String>) {
    var port = 4500
    val server = embeddedServer(Netty, port) {
        routing {
            get("/") {
                call.respondText("""{"data": "Hello World!"}""", ContentType.Application.Json)
            }
        }
    }
    server.start(wait = true)
}